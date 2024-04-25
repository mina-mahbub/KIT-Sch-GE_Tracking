import numpy as np
import os
from PIL import Image
from tqdm import tqdm
from scipy.spatial.distance import cdist
import numba
import argparse
import concurrent.futures

@numba.njit()
def get_cell_centers(seg):
    labels = np.unique(seg)
    centers = np.zeros((labels.shape[0]-1, 2))
    idx = 0
    for label in labels:
        if label != 0:
            inds = np.argwhere(seg == label)
            loc_x = np.mean(inds[:, 0])
            loc_y = np.mean(inds[:, 1])
            centers[idx, 0] = loc_x
            centers[idx, 1] = loc_y
            idx += 1
    return centers

def calculate_score(gt_centers, pred_centers):
    mean_dist = np.mean(cdist(gt_centers, pred_centers).min(0))
    diff_cells = pred_centers.shape[0] - gt_centers.shape[0]
    return mean_dist, diff_cells

def count_frames(gt_folder, targ_ext=['.tif']):
    total = 0
    for filename in os.listdir(gt_folder):
        fname, ext = os.path.splitext(filename)
        if ext in targ_ext:
            total += 1
    return total

def open_frame(frame, folder, name_root, num_digits):
    filename = f"{name_root}{frame:0{num_digits}d}.tif"
    seg = Image.open(os.path.join(folder, filename))
    return np.array(seg)

def process_frame(frame, gt_folder, pred_folder, name_root_gt, name_root_pred, num_digits):
    gt_frame = open_frame(frame, gt_folder, name_root_gt, num_digits)
    seg_frame = open_frame(frame, pred_folder, name_root_pred, num_digits)
    gt_centers = get_cell_centers(gt_frame)
    seg_centers = get_cell_centers(seg_frame)
    score, delta = calculate_score(gt_centers, seg_centers)
    return frame, score, delta

def main(gt_folder, pred_folder, num_digits, num_processes):
    n_frames = count_frames(gt_folder)
    name_root_gt = "man_seg"
    name_root_pred = "mask"

    scores = []
    deltas = []

    with concurrent.futures.ProcessPoolExecutor(max_workers=num_processes) as executor:
        futures = [executor.submit(process_frame, frame, gt_folder, pred_folder, name_root_gt, name_root_pred, num_digits) for frame in range(n_frames)]
        for future in tqdm(concurrent.futures.as_completed(futures), total=n_frames, desc="Processing Frames"):
            frame, score, delta = future.result()
            scores.append(score)
            deltas.append(delta)

    print(f"Average Score: {np.mean(scores):.6f}")
    print(f"Average Count Difference: {np.mean(deltas):.6f}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate scores from image segmentation.")
    parser.add_argument("root_folder", type=str, help="Path to where the images are")
    parser.add_argument("number", type=str, help="number of sequence to evaluate")
    parser.add_argument("num_digits", type=int, help='number of leading 0s in file name')
    parser.add_argument("--processes", type=int, default=24, help="Number of processes to use")
    args = parser.parse_args()

    gt_folder = os.path.join(args.root_folder, f"{args.number}_GT", "SEG")
    pred_folder = os.path.join(args.root_folder, f"{args.number}_RES")
    main(gt_folder, pred_folder, args.num_digits, args.processes)


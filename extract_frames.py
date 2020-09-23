import argparse
from cv2 import cv2
 
def extract_frames(video_path, save_folder, max_frames):
    cap= cv2.VideoCapture(video_path)
    i=0
    while(cap.isOpened() and i < int(max_frames)):
        ret, frame = cap.read()
        if ret == False:
            break
        cv2.imwrite(save_folder+str(i)+'.jpg',frame)
        print('Saved frame {0}'.format(i))
        i+=1
    
    cap.release()
    cv2.destroyAllWindows()


def parse_args():
    """Parse command line arguments.
    """
    parser = argparse.ArgumentParser(description="Extracting frames from videos")
    parser.add_argument(
        "--video_path",
        default="./test_sheep.mpg",
        help="Path to video (to extract frames)")
    parser.add_argument(
        "--save_folder",
        default="./sheep-test/test-1/img1/",
        help="Folder path to save frames")
    parser.add_argument(
        "--max_frames",
        default=float('inf'),
        help="Maximum number of frames to save"
    )
    return parser.parse_args()


def main():
    args = parse_args()
    extract_frames(args.video_path, args.save_folder, args.max_frames)


if __name__ == '__main__':
    main()
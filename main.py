import cv2 as cv
import argparse
import os
from os import path as path


# ASCII chars representing pixels

chars = " .,:;=!%#&@"


def main():

    # Arguments parsing

    parser = argparse.ArgumentParser(description="Convert images/video to ASCII art")
    parser.add_argument("--inputpath", type=str, help="path of the input video or image sequence")
    parser.add_argument("--nameformat", type=str, help="name format of the image sequence (i.e. \"frame_\")", default="")
    parser.add_argument("--firstframe", type=int, help="number of the first frame", default=0)
    parser.add_argument("--filetype", type=str, help="filetype of input image", default="jpg")
    parser.add_argument("--resolution", type=int, help="amount of times the image's resolution is going to be divided", default=16)
    args = parser.parse_args()


    # Open input file(s)

    # Invalid input path
    if not path.exists(args.inputpath):
        print(args.inputpath)
        print("Invalid input path")
        print("Exiting program")
        exit()


    # Input is video
    if path.isfile(args.inputpath):
        
        try:
            input_video = cv.VideoCapture(args.inputpath)
        except:
            print("Input is neither a video nor an image sequence")
            print("Exiting program")
            exit()


        while True:
            success, frame = input_video.read()

            if not success:
                break
            
            print(process_frame(frame, args.resolution))
            cv.waitKey(50)

    # Input is image sequence
    else:

        frame_num = args.firstframe
        filename = args.inputpath + args.nameformat + str(frame_num) + args.filetype

        while path.exists(filename):
            frame = cv.imread(filename)
            print(process_frame(frame, args.resolution))
            cv.waitKey(50)
            frame_num += 1


# Print frame as ASCII characters in console
def process_frame(frame, resolution):

    frame = cv.resize(frame, (frame.shape[1]//resolution, frame.shape[0]//resolution))
    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    result = ""

    dimensions = frame.shape

    for y in range(dimensions[0]):
        for x in range(dimensions[1]):
            pxl = frame[y][x]
            result += chars[int(pxl/255*(len(chars)-1))] + " "
        result += "\n"

    return result

main()
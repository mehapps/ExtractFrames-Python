if __name__ == "__main__":
    print("Please do not run this as a script!")
    exit()
else:
    def frames(dir_path, video_path):
        import cv2, moviepy.editor
        cam = cv2.VideoCapture(video_path)
        i = -1
        while True:
            i += 1
            ret, frame = cam.read()
            if ret:
                name = dir_path + str(i) + '.jpg'
                print ('Creating ' + name)
                cv2.imwrite(name, frame)
                print("Created " + name)
            else:
                cam.release()
                cv2.destroyAllWindows()
                break
from imageai.Detection import VideoObjectDetection
import os
import cv2

def forFrame(frame_number, output_array, output_count):
    print("FOR FRAME " , frame_number)
    print("Output for each object : ", output_array)
    print("Output count for unique objects : ", output_count)
    print("------------END OF A FRAME --------------")

camera = cv2.VideoCapture(0)
execution_path = os.getcwd()


while(camera.isOpened()):
    ret,frame = camera.read()
    detector = VideoObjectDetection()
    cv2.imshow("Frame",camera)
    #print(frame)
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
    detector.loadModel()
    video_path = detector.detectObjectsFromVideo(camera_input=camera,
                                output_file_path=os.path.join(execution_path, "camera_detected_video")
                                , frames_per_second=5, log_progress=True, minimum_percentage_probability=60)
    cv2.imshow("Frame",frame)
    if cv2.waitKey(1) & 0xFF == ord ('q'):
        break
    else:
        capture.release()
        cv2.destroyAllWindows()
        break
print(video_path)
    

from mmdet.apis import init_detector, inference_detector, show_result_pyplot
import mmcv
import os
import glob

if 1:  # fasterrcnn
    config_file = '../../configs/hackathon/faster_rcnn_r50_fpn_1x_car_damage_1cat.py'
    checkpoint_file = '/home/dalya/PycharmProjects/mmdet/mmdetection/results/overfit_1cat_exp1/epoch_15.pth'
else:  # retinanet
    config_file = '../../configs/hackathon/retinanet_r50_fpn_1x_car_damage_1cat.py'
    checkpoint_file = '/home/dalya/PycharmProjects/mmdet/mmdetection/results/overfit_1cat_exp2/epoch_15.pth'


# build the model from a config file and a checkpoint file
model = init_detector(config_file, checkpoint_file, device='cuda:0')

# test a single image
images_path = '/home/dalya/PycharmProjects/mmdet/mmdetection/data/car_damage/train/'
images_list = glob.glob(images_path + '*.jpg')
for img_path in images_list:
    result = inference_detector(model, img_path)

    # show the results
    show_result_pyplot(model, img_path, result)
    aaa = 1

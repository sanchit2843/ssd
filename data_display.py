import pandas as pd
data = pd.read_csv(path_bbox)
name = data.iloc[:,0].values
label = data.iloc[:,1].values
bbox = data.iloc[:,2:6].values
def img_read(path,target_size):
  image = cv2.imread(path)
  shape = image.shape
  image = cv2.resize(image,(target_size,target_size))
  return image,shape
def n_boxes(img_name, bbox , name):
  bbox_n = list()
  for i in range(len(name)):
    if(name[i] == img_name):
      bbox_n.append(bbox[i])
  return bbox_n
def rescale_bbox(bbox:list , shape , target_size = 224):
  for i in range(len(bbox)):
    x_scale = target_size/shape[1]
    y_scale = target_size/shape[0]
    bbox[i][0] = int(round(bbox[i][0]*x_scale))
    bbox[i][1] = int(round(bbox[i][1]*y_scale))
    bbox[i][2] = int(round(bbox[i][2]*x_scale))
    bbox[i][3] = int(round(bbox[i][3]*y_scale))
  return bbox
def draw_boxes(img_name, boxes: list):
    img_name = '/content/train/' + img_name
    a = list()
    a.append(boxes)
    img,_ = img_read(img_name)
    for box in a:
        cv2.rectangle(img, (box[0],box[1]),((box[0]+box[2]),(box[1]+box[3])),(0, 0, 255), 2)
    return img
#reshape all bounding boxes in file
from tqdm import tqdm
for i in tqdm(range(len(name))):
  img_name = '/content/train/' + name[i]
  box = bbox[i,:]
  image = cv2.imread(img_name)
  shape = image.shape
  a = list()
  a.append(box)
  box = rescale_bbox(a,shape)
  box = np.asarray(box)
  bbox[i,:] = box

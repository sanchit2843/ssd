def iou(box_true,box_pred , train = False):
  xA = max(box_true[0] , box_pred[0])
  yA = max(box_true[1] , box_pred[1])
  x_true = box_true[0] + box_true[2]
  y_true = box_true[1] + box_true[3]
  x_pred = box_pred[0] + box_pred[2]
  y_pred = box_pred[1] + box_pred[3]
  xB = min(x_true , x_pred)
  yB = min(y_true , y_pred)
  interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)
  boxAArea = (box_true[2])*(box_true[3])
  boxBArea = (box_pred[2])*(box_pred[3])
  iou = interArea / float(boxAArea + boxBArea - interArea)
  return iou
'''
To do ->
Focal loss
Non max suppression
'''

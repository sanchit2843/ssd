import xml.etree.ElementTree as ET
data = []
from tqdm import tqdm
for i in tqdm(os.listdir(root_dir)):
    path = os.path.join(root_dir,i)
    tree = ET.parse(path)
    root = tree.getroot()
    objects = root.findall('object')
    a = len(objects)
    for obj in objects:
        name = obj.findall('name')[0].text
        fname = root.findall('filename')[0].text
        xmax = obj.findall('bndbox')[0].findall('xmax')[0].text
        xmin = obj.findall('bndbox')[0].findall('xmin')[0].text
        ymax = obj.findall('bndbox')[0].findall('ymax')[0].text
        ymin = obj.findall('bndbox')[0].findall('ymin')[0].text
        data.append([fname,name, xmin, ymin, xmax, ymax])
df = pd.DataFrame(data, columns=['fname', 'class_name','xmin', 'ymin', 'xmax', 'ymax'])
data = df.sort_values(by = 'fname')

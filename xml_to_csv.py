"""

Disclaimer: Not my code, but was used as part of implementation.
From: https://github.com/datitran/raccoon_dataset

"""
import os
import glob
import pandas as pd
import argparse
import xml.etree.ElementTree as ET


def xml_to_csv(path):
    classes_names = []
    xml_list = []
    for xml_file in glob.glob(path + "/*.xml"):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall("object"):
            classes_names.append(member[0].text)
            value = (
                root.find("filename").text,
                int(root.find("size")[0].text),
                int(root.find("size")[1].text),
                member[0].text,
                int(member[4][0].text),
                int(member[4][1].text),
                int(member[4][2].text),
                int(member[4][3].text),
            )
            xml_list.append(value)
    column_name = [
        "filename",
        "width",
        "height",
        "class",
        "xmin",
        "ymin",
        "xmax",
        "ymax",
    ]
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    classes_names = list(set(classes_names))
    classes_names.sort()
    return xml_df, classes_names
    
    
def main():
    for folder in ['train','test']:
        image_path = os.path.join(os.getcwd(), ('data/' + folder))
        xml_df = xml_to_csv(image_path)
        xml_df.to_csv(('annotations/' + folder + '_labels.csv'), index=None)
        print('Successfully converted xml to csv.')


main()

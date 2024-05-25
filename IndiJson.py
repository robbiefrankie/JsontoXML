import os
import json
import xml.dom.minidom
import xmltodict
 
def clean_invalid_xml_characters(xml_str):
    cleaned_chars = []
    for char in xml_str:
        if char == '&':
            cleaned_chars.append('&amp;')
        elif char == '<':
            cleaned_chars.append('&lt;')
        elif char == '>':
            cleaned_chars.append('&gt;')
        elif ord(char) > 0x7e:
            cleaned_chars.append('&#{};'.format(ord(char)))
        else:
            cleaned_chars.append(char)
    return ''.join(cleaned_chars)
 
def json_to_xml(json_data):
    try:
        # Convert JSON to XML using xmltodict
        xml_data = xmltodict.unparse(json_data, pretty=True)
        return xml_data
    except Exception as e:
        print(f"Error converting JSON to XML: {e}")
        return None
 
def process_files(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        if filename.endswith('.json'):
            with open(os.path.join(input_folder, filename), 'r') as json_file:
                try:
                    json_data = json.load(json_file)
                    xml_data = json_to_xml(json_data)
                    if xml_data is not None:
                        output_filename = os.path.splitext(filename)[0] + '.xml'
                        output_path = os.path.join(output_folder, output_filename)
                        with open(output_path, 'w') as xml_file:
                            xml_file.write(xml_data)
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON in {os.path.join(input_folder, filename)}: {e}")
                except Exception as e:
                    print(f"Error processing {os.path.join(input_folder, filename)}: {e}")
 
def main():
    input_folder = "C:\\Users\\PRobert\\Documents\\JSON2XML\\Input_Folder"
    output_folder = "C:\\Users\\PRobert\\Documents\\JSON2XML\\Output_Folder"
    process_files(input_folder, output_folder)
 
if __name__ == "__main__":
    main()
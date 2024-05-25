import os
import json
import xml.etree.ElementTree as ET
import xml.dom.minidom

def json_to_xml(json_data):
    root_name = next(iter(json_data))
    root = ET.Element(root_name)
    json_to_xml_recursive(json_data[root_name], root)
    xml_str = ET.tostring(root, encoding='unicode')
    # Use minidom to pretty print the XML
    xml_str_pretty = xml.dom.minidom.parseString(xml_str).toprettyxml()
    return xml_str_pretty

def json_to_xml_recursive(json_data, xml_parent):
    for key, value in json_data.items():
        if isinstance(value, dict):
            child = ET.SubElement(xml_parent, key)
            json_to_xml_recursive(value, child)
        elif isinstance(value, list):
            for item in value:
                child = ET.SubElement(xml_parent, key)
                json_to_xml_recursive(item, child)
        else:
            ET.SubElement(xml_parent, key).text = str(value)

def process_files(input_folder, output_folder):
    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Process each file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".json"):
            input_file_path = os.path.join(input_folder, filename)
            output_file_path = os.path.join(output_folder, filename[:-5] + ".xml")

            # Read JSON data from file
            with open(input_file_path, 'r') as file:
                # Open output file in append mode
                with open(output_file_path, 'a') as xml_file:
                    # Process each line as a JSON object
                    for line in file:
                        try:
                            jsondata = json.loads(line)
                        except json.JSONDecodeError as e:
                            print(f"Error decoding JSON in {input_file_path}: {e}")
                            continue

                        # Convert JSON to XML
                        xml_data = json_to_xml(jsondata)

                        # Write XML data to file
                        xml_file.write(xml_data)

def main():
    input_folder = r"C:\Users\PRobert\Documents\JSON2XML\BatchJson_Input"
    output_folder = r"C:\Users\PRobert\Documents\JSON2XML\BatchJson_Output"
    process_files(input_folder, output_folder)

if __name__ == "__main__":
    main()

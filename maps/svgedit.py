import xml.etree.ElementTree as ET
import random
import hjson
from cairosvg import svg2png
import subprocess
et = ET.parse('earth8kt.svg')
# Get svg
root = et.getroot().findall('{http://www.w3.org/2000/svg}g')[0]
label = '{http://www.inkscape.org/namespaces/inkscape}label'
color_list = {}

for k in root:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_list[k.attrib[label]] = (r, g, b)
    color_text = '#%02x%02x%02x' % (r, g, b)
    style_text = k.attrib['style'] = "display:inline;stroke:#000000;stroke-opacity:1;stroke-width:0;stroke-dasharray:none;fill:{};fill-opacity:1".format(color_text)
    k.attrib['style'] = style_text
    # Get all children
    for b in k.iter():
        b.attrib['style'] = style_text
    # Change the color, I guess
    # Change the color
    # color_list[k.attrib[label]] = 
'''for k in root.findall('{http://www.w3.org/2000/svg}g'):
    print(k.attrib['id'])
    # Edit the thing
    for country_element in k.findall('{http://www.w3.org/2000/svg}g'):
        print(k.attrib['{http://www.inkscape.org/namespaces/inkscape}label'])
    #print(k.attrib['{http://www.inkscape.org/namespaces/inkscape}label'])
    # Then if it's a country then '''
OUTPUT_SVG_NAME = 'output.svg'
OUTPUT_HJSON_NAME = 'color_list.hjson'
OUTPUT_PNG_NAME = 'output.png'
et.write(OUTPUT_SVG_NAME)

# Output to hjson
# Format the hjson content
hjson_content = {}
for item in color_list:
    hjson_content[item] = hjson.OrderedDict([('color', color_list[item])])
f = open(OUTPUT_HJSON_NAME, "w")
f.write(hjson.dumps(hjson_content))
f.close()

# Output svg
subprocess.run(['inkscape', OUTPUT_SVG_NAME, '-o', OUTPUT_PNG_NAME])

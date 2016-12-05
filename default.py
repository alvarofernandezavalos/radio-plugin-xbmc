import os
import sys
import plugintools
import urllib2

# Entry point
def run():
    plugintools.log("radihans.run")

    # Get params
    params = plugintools.get_params()

    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"

    plugintools.close_item_list()

# Main menu
def main_list(params):
        response = urllib2.urlopen('https://dl.dropboxusercontent.com/s/w9m6ivj70i5fgyg/list_radio.xml')
        with open(os.path.dirname(os.path.realpath(__file__))+'/list_radio.xml','wb') as output:
            output.write(response.read())
        import xml.etree.ElementTree as ET
        tree = ET.parse(os.path.dirname(os.path.realpath(__file__))+'/list_radio.xml')
        root = tree.getroot()
        for radio in root.findall('radio'):
                title = radio.find('title').text
                plot = radio.find('plot').text
                url = radio.find('url').text
                thumbnail = radio.find('thumbnail').text
                plugintools.add_item( action="play" , title=title , plot=plot , url=url ,thumbnail=thumbnail , isPlayable=True, folder=False )
        plugintools.sort_list()

def play(params):
    plugintools.play_resolved_url( params.get("url") )

run()
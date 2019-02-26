# CERT-ISSUER

In this module, the edited files are ```certificate_storage_bridge.py``` and ```award.html```.
A little script was added to make our flask application support the rendering of ```displayHtml``` field inside our certificate.

**certificate_storage_bridge.py**: edited to call our script. (1 line was added)<br/>
**award.html**: edited to add the redering of our custom field.<br/>
**displayHtml.py**: is a little script that retrieves the selected certificate, parses the json to return its ```displayHtml``` value.

# Link to original files
**certificate_storage_bridge.py**: https://github.com/blockchain-certificates/cert-viewer/blob/master/cert_viewer/certificate_store_bridge.py
**award.html**: https://github.com/blockchain-certificates/cert-viewer/blob/master/cert_viewer/templates/award.html

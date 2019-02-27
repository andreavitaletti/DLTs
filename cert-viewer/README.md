# CERT-VIEWER

In this module, the edited files are ```certificate_storage_bridge.py``` and ```award.html```.
A little script was added to make flask application support the rendering of ```displayHtml``` field inside the certificate.

**certificate_storage_bridge.py**: edited to call our script (1 line was added).<br/>
**award.html**: edited to add the redering of ```displayHtml``` field.<br/>
**displayHtml.py**: is a little script that retrieves the selected certificate and parses the json to return its ```displayHtml``` value.

### Link to original files
**certificate_storage_bridge.py**: https://github.com/blockchain-certificates/cert-viewer/blob/master/cert_viewer/certificate_store_bridge.py<br/>
**award.html**: https://github.com/blockchain-certificates/cert-viewer/blob/master/cert_viewer/templates/award.html

# CERT-TOOLS

The edited file in this module are ```conf.ini``` and ```roster_testnet.csv```<br/>
**conf.ini** file can be filled changing:<br/>
* ```issuer_id```: here you need to put the url for a static issuer.json file created with ```certificate-issuer``` script.
* ```issuer_signature_line```: replace ```<name of issuer signature image>``` to corresponding file name inside ```image``` folder.
* ```badge_id```: can be leaved with default value of original file. Default: ```82a4c9f2-3588-457b-80ea-da695571b8fc```
* ```issuer_logo_file```, ```cert_image_file```, ```issuer_signature_file```: replace tags with name of each relative image inside the ```images``` folder.
* ```additional_global_fields```: We are adding a schema definition to make certificate support our additional custom fields. (Added an example to link the schema definition using a static url to a json file.)
*```additional_per_recipient_fields```: Adding custom per recipient fileds parsed from roster file.

**roaster_testnet.csv** has 4 additional column with our custom definition.

# Path to original files
**conf.ini**: https://github.com/blockchain-certificates/cert-tools/blob/master/conf.ini
**roaster_testnet.csv**: https://github.com/blockchain-certificates/cert-tools/blob/master/sample_data/rosters/roster_testnet.csv

# gam.domain
--
A script to assist with switching OAuth files for GAM when using miltiple Google Workspace instances.
--


1) Place both the domain.txt and gam.domain.py files into GAM's installed directory.

2) Open up gam.domain.py and fill in variables with the domain information and Oauth file directories.
  - Note: You will need to create new GAM projects for each domain, then copy the oauth2.txt, oauth2service.json, and client_secrets.json into a folder.
  - This folder will be the location for the domain_folder variables.

# raptor remote proxy for utorrent/bittorrent remote :-)

**DO NOT USE `localhost` ANYWHERE**

Ubuntu: (if you are using MAC OS X, please refer: https://github.com/bittorrent/raptor/blob/master/README_OS_X.markdown)

1. Install Git.
  	1. `apt-get install git-core`

2. Clone https://github.com/bittorrent/raptor

3. Clone https://github.com/bittorrent/talonstatic
	1. `cd talonstatic`
	2. `git submodule init`
	3. `git submodule update`

4. install pip & virtualenv
	1. `sudo apt-get install python-pip python-dev build-essential`
	2. `sudo pip install --upgrade pip`
	3. `sudo pip install --upgrade virtualenv`

5. install python2.6 dev header
	1. `apt-get install python2.6-dev`

6. cd into talonstatic/static directory
	1. `ln -s ../webui webui`,creates symbolic link `static/webui` pointing to the webui 	submodule inside talonstatic 

7. cd into raptor directory

8. Try to recreate all the steps in build.sh (the `g++` commands are not necessary nor the nginx and stunnel configurations)
	1. if python2.6 doesn't exist for your version of ubuntu, install python2.6 via `apt-get install python2.6`

9. Modify the **very secret** advanced settings in µTorrent (Windows client only: launch it with `shift+F2` and keep pressing key combo while opening Options > Preferences)

  		webui.raptor_host		{LOCAL IP}
		webui.raptor_port		9050
		webui.raptor_secure		false
		webui.talon_host		{LOCAL IP}
		webui.talon_port		9090

10. Run the following command from the raptor directory:

		_install/bin/python -m raptor.serve --debug=1 --disable_catn=1 --attach_hostname={LOCAL IP} --dont_have_nginx=1 --logout_root=http://{LOCAL IP}:9090 --static_content_path={TALONSTATIC DIR}/static --static_content_path_tablet={TABLETUI DIR} --templates_path={RAPTOR DIR}/templates
		
		\* the tabletui setting can be removed

11. After you run the command you should be able to login on your browser, open:

		http://{LOCAL IP}:9090/srp?noredirect=1

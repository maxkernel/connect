from fabric.api import run, settings, env
from fabric.context_managers import cd
from fabric.operations import put

from os.path import basename

CONFIG		= {
	'deploy_path'	:	'.deploy',
	'default_cmd'	:	'sh .run',
}

def deploy(path, name=None, cmd=CONFIG['default_cmd'], autostart=True):
	global CONFIG
	
	if name == None:
		name = basename(path)
	
	args = dict(CONFIG.items() + {'name': name, 'cmd': cmd}.items())
	
	with settings(warn_only=True):
		run('mkdir ~/%(deploy_path)s' % args)
		run('max-client -k')
		put(path, '~/%(deploy_path)s/%(name)s' % args)
	
		if autostart:
			run('max-autostart -- max-client --archive=$HOME/%(deploy_path)s/%(name)s %(cmd)s' % args)
	
		run('max-client --daemon --archive=$HOME/%(deploy_path)s/%(name)s %(cmd)s' % args)
	



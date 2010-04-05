import os

uname = ''
try:
    uname = os.uname()[0]
except:
    pass

def getopenldapenv(options,buildout):
    #on everything else than linux patch configure too
    if uname in ['Darwin', 'FreeBSD']:
        cmd1 = "gsed \
                -e 's|-lsasl2||' \
                -e 's|-lsasl||' \
                -i %s/configure" % (options['compile-directory'])

        if os.system(cmd1):
                raise Error('System error')

    if uname in ['Linux']:
        os.environ['CPPFLAGS'] = '%s %s' % (os.environ.get('CPPFLAGS', ''), ' -D_GNU_SOURCE ')

# vim:set ts=4 sts=4 et  :

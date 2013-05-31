import os

uname = ''
try:
    uname = os.uname()[0]
except:
    pass

def getopenldapenv(options,buildout):
    #on everything else than linux patch configure too
    if uname in ['FreeBSD']:
        cmd1 = ("gsed "
                " -e 's|-lsasl2||'" 
                " -e 's|-lsasl||'" 
                " -i %s/configure") % (options['compile-directory'])
    if uname in ['Darwin']:
        cmd1 = ("sed -iE 's/-lsasl2//g'  %(c)s/configure;" 
                "sed -iE 's/-lsasl//g'   %(c)s/configure;")%{'c':options['compile-directory']}
    if uname in ['Darwin', 'FreeBSD']:
        print "Running %s" % cmd1
        if os.system(cmd1):
            raise Exception('System error: %s' % cmd1)

    if uname in ['Linux']:
        os.environ['CPPFLAGS'] = '%s %s' % (os.environ.get('CPPFLAGS', ''), ' -D_GNU_SOURCE ')

# vim:set ts=4 sts=4 et  :

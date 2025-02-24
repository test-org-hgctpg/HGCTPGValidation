def run() {
    sh '''
    set +x
    echo '==> Install automatic validation package HGCTPGValidation. ============================'
    exec >> log_Jenkins
    echo '==> Install automatic validation package HGCTPGValidation. ============================'
    uname -a
    whoami
    pwd
    ls -l
    if [ -d "./HGCTPGValidation" ] 
    then
        rm -rf HGCTPGValidation
    fi
    git clone -b ${BRANCH_HGCTPGVAL} https://github.com/${REMOTE_HGCTPGVAL}/HGCTPGValidation HGCTPGValidation
    source HGCTPGValidation/env_install.sh
    pip install attrs
    if [ -d "./test_dir" ] 
    then
        echo "Directory test_dir exists."
        rm -rf test_dir
    fi
    mkdir test_dir
     ls -lrt ..
    echo '   '
    '''
}

return this

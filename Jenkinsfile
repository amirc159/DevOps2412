properties([pipelineTriggers([pollSCM('* * * * *')])])
node {
    stage("clone") {
        git branch: 'master', url: 'https://github.com/amirc159/DevOps2412.git'
    }
    stage("show files"){
        sh "ls -l"
    }
}

import groovy.transform.Field

import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.Set;
import java.util.HashSet;
import java.util.List;
import java.util.ArrayList;


def uploadGrafana () {
    withCredentials([usernamePassword( credentialsId: 'myCredentials', usernameVariable: 'MYUSER', passwordVariable: 'MYPWD' )]) {
        sh """#!/bin/bash
            apt-get update; apt -y install python3-pip; pip install requests
            python3 upload_to_grafana.py
        """.stripIndent()
    }
}

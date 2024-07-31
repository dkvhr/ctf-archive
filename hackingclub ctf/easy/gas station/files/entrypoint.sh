#!/bin/bash

su -s /bin/bash nobody -c "socat TCP-LISTEN:1337,fork EXEC:'/app/program'"
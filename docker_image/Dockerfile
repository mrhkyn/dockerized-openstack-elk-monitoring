FROM ubuntu:latest  
RUN apt-get update  
RUN apt-get install --no-install-recommends --no-install-suggests -y mariadb-client python-mysqldb  
ENV ExecPythonName TenantIpMatchList.py  
ENV OutputName TenantIpMatches.yaml
WORKDIR /SOURCE  
CMD sh -c "python /SRC/$ExecPythonName /RES/$OutputName"


#BUILDER
FROM alpine:3.19.1 as builder

ARG version="energi3-v1.1.7-linux-armv8"
ENV version=${version}

WORKDIR /opt/energi

#Install curl and Pert Utils shasum
RUN apk --no-cache add curl && \
    apk --no-cache add perl-utils 

#Download Energi Linux and SHA265SUMS
RUN curl https://s3-us-west-2.amazonaws.com/download.energi.software/releases/energi3/v1.1.7/$version.tgz \
    --output energi3-v1.1.7-linux-armv8.tgz
RUN curl https://s3-us-west-2.amazonaws.com/download.energi.software/releases/energi3/v1.1.7/SHA256SUMS \
    --output SHA256SUMS

#Check SHA256
RUN shasum -a 256 -c SHA256SUMS --ignore-missing

#Extract energi3 to /opt/energi/extract
RUN tar -xvzf $version.tgz 
RUN mkdir extract && mv $version/bin/energi3 extract



#APP Energi
FROM ubuntu:24.04 as app

#Non-root energi user
RUN groupadd -r energi
RUN useradd -r -g energi -m energi

#set the working directory to /app
WORKDIR /app/energi
RUN chown -R energi /app/energi

#Copy energi app from Builder
COPY --from=builder /opt/energi/extract/energi3 /app/energi/bin/

# Set the non-root user as the default user
USER energi

ENTRYPOINT ["/bin/bash","-c","/app/energi/bin/energi3"]
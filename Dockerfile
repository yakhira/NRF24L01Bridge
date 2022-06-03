ARG BUILD_FROM
FROM $BUILD_FROM

ENV WORKDIR /data
ENV APPDIR /app
ENV LANG C.UTF-8

COPY app/ $APPDIR/

WORKDIR $WORKDIR

RUN apk add --no-cache py3-pip python3-dev musl-dev gcc linux-headers; \
    pip install --no-cache-dir -r $APPDIR/requirements.txt; \
    chmod +x $APPDIR/run.sh

LABEL \
    io.hass.name="NRF24L01 Bridge" \
    io.hass.description="NRF24L01 Bridge." \
    io.hass.arch="${BUILD_ARCH}" \
    io.hass.type="addon" \
    io.hass.version=${BUILD_VERSION} \
    maintainer="Ruslan Iakhin <ruslan.k.yakhin@gmail.com>"

ENTRYPOINT ["/app/run.sh"]
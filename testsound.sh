# record a 3 second clip at CD quality and play it back
echo "RECORDING..."
arecord -d 3 -f cd test.wav
echo "PLAYBACK..."
aplay test.wav

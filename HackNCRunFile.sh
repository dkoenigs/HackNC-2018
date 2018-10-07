java -jar HackNC18Runnable.jar %* > output.txt
cat output.txt | python play-model-v2.py

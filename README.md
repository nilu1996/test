https://www.oracle.com/java/technologies/downloads/#java11

tar -xzvf jdk-11.0.11_linux-x64_bin.tar.gz

sudo mv jdk-11.0.11 /usr/local/

nano ~/.bashrc

export JAVA_HOME=/usr/local/jdk-11.0.11
export PATH=$JAVA_HOME/bin:$PATH

source ~/.bashrc

java --version

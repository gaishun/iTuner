\# iTuner

For iTuner SC 23



iTuner-5.8.tar.xz is the source code of `iTuner` kernel;

```shell
xz -d iTuner-5.8.tar.xz
tar -x iTuner-5.8.tar
mv linux-5.8 linux-5.8-iTuner
```

original-5.8.tar.gz is the source code of the original linux kernel 5.8

```shell
tar zxvf original-5.8.tar.gz
mv linux-5.8 linux-5.8-original
```



The file `statistic` is a script used to statistic the interruptions issue by a identified device from the file `/proc/interrupts`

```shell
statistic $DEVICE_NAME$

#EX: statistic the interruptions from device nvme0
statistic nvme0
```


# IOS_SHOGUN-Colorful

'IOS_ SHOGUN's Java development framework colorful @ is copyrighted by Atomic and 'IOS_SHOGUN' All developers have a tag: 'colorful-Frame'|

[Github-flavored Java version](https://github.com/Atomicntege/IOS_SHOGUN/)
|
In this folder 'API-Content' contains some basic tutorials that will help you understand the colorful framework

2023-2-16 When we updated, we fixed some minor issues:

**repair** :**1**.The SequenceCachedPool vector mode, saturation strategy, worker being suspended, unable to recycle after shutdown state has been fixed in 2.14.
Let's briefly show the vulnerability Below is my test code(Now available):

        SequenceCachedPool Test=new SequenceCachedPool(2,3,100, TimeUnit.MILLISECONDS,
                new LinkedBlockingDeque<>(10));

        SequenceCachedPool.VectorModeRejected Vector=new SequenceCachedPool.VectorModeRejected(Test){
            @Override
            protected void EnforcementDisconnection(Throwable t) {
                super.EnforcementDisconnection(t);
                console.Info(t);
            }

            @Override
            protected void disconnection(Runnable T, Throwable t) {
                super.disconnection(T, t);
                console.Info(t);
            }
            //A rare exception when running vector mode in both ways
            //But in the end nothing happened
        };
        
        Test.vectorMode(Vector);
        
        IntStream.range(1,1000).forEach(DATA->{
            if(DATA==999) {
                Test.shutdown();
                Test.submit(() -> console.log(DATA));
            }
        });
----------------
|**repair** :**2**.Fixed the problem that the interface was not disclosed in the highly parallelized Promise Seed Task Waterfall 1.0.

        SequenceCachedPool Test = new SequenceCachedPool(2, 3, 100, TimeUnit.MILLISECONDS,
        new LinkedBlockingDeque<>(10));
        TaskSeed<Integer> Test2 = new TaskSeed<>(Test);
        Test2.RunBean(() -> {
            console.info("seed task1!");
            Test2.setThen(10);
        }).Then((value) -> () -> console.info("seed task2!" + (value << 2)));
        Test.shutdown();
----------------
Main update2023-2-20Update content:

Minor update - Colorful1.0 - TaskList 1.0 connector - split join - polymorphism collection iteration, ingesting arrays, toInjection, LocalXmlDocument, JXpathExpression, ordered

JTO-Update Ordering-LAX_Huffman-LAX Parsed Huffman Data Compression Structure--JTO-Ordered LAXTranslating
__response--Update--Name optimization-Update:

    _Export
    _Hex_byte
    T_X16_X16_D
    D_X16_X16_T
    T_X16_X16_D_Speak
    Text_X16_T
    I_x_36_
    T_x_X36_i
    D_X2_X16_T
    D_X2_X16_D
    T_X16_X2_D
    X16_X10
    X10_byte
    byte_X10
    T_x_X2_X10_T
    T_x_X10_X2_T
    T_x_X2_X10_L
    T_x_X10_X2_L
    I_x_X2_X10_L
    I_x_X10_X2_L
    X_LAX
    L_Hfm
    D_X2_X16_T_S
    T_X16_X36_T
    T_X36_X16_T
    T_X2_X2_D
    D_HUM_X2_T
    D_X2_UTF_8_T
    D_X2_UTF_8_D
    D_X2_ASCII_T
    D_X2_ASCII_D
    T_X2_UTF_8_T
    T_X2_UTF_8_D
    T_X2_ASCII_T
    T_X2_ASCII_D
    S_A
    1.0 and other interfaces

Basic use of exhibits:
    1.

    IOS_SHOGUN_Toolkit ios_shogun=new IOS_SHOGUN_Toolkit();

Basic use of exhibits:
    2.

    //LAX parsing
    JTO.LAX("[A,B,C,1,2,3,A=12]").SeeTask();
    //JSON to JTO collection
    JTO.JSONParser("{ios-shogun:{shogun:ABC}}").SeeAll();
    //JTO to JSON
    console.log(JTO.toJSON(JTO.JSONParser("{ios-shogun:600}")));
    //...

Basic use of exhibits:
    3.
    
        IOS_SHOGUN_Toolkit SHOGUN=new IOS_SHOGUN_Toolkit();
        SHOGUN.NET_GET("URL", (Facet_injections) -> {
            Facet_injections.UpgradeToEncrypt();//HTTP->HTTPS
            Facet_injections.UpdateConnection();//Update connect
            //Facet_injections.CancelEvent();//cancel event
            Facet_injections.UA_injection("Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36");
            Facet_injections.collectivity(
                    """
                       "Cookie":"...You",
                       "Content-Type": "application/json; charset=utf-8"
                       //HTTP    
                    """);
        }, (SourceData) -> new CachedTask<>() {
            //Event
            //Callback events
            //Data->SourceData
            __request r=SourceData.get__Requests();
            __response r2=SourceData.get__Responses();
        });

Basic use of exhibits:
    MD5 4.
    
            IOS_SHOGUN_Toolkit SHOGUN=new IOS_SHOGUN_Toolkit();
        console.info(SHOGUN.MD5HashEncryption("ABC"));
        //output->902FBDD2B1DF0C4F70B4A5D23525E932
        SHOGUN.MD5FingerprintComparison("MD5 contrast","MD5 contrast");

Basic use of exhibits:
    PS Image Simple: Example:
        
        IOS_SHOGUN_Toolkit SHOGUN=new IOS_SHOGUN_Toolkit();
        ImageChannel IC=new ImageChannel(A-> {
            try {
                return SHOGUN.Src_Graphics_bf("Image path");
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        });
        //A simple image planet that can be used containing a very large number of image channels
        AdjustmentChannel AC=new AdjustmentChannel(IC,0);
        //Simple auxiliary channel
        AC.AdjustmentCommandHue(100);
        //Hue instruction

        byte[] bytes=ImageChannel.getByteData(IC,0).toByteArray();
        //IC--ImageChannel,index-0=Identity card
        //AdjustmentChannel->byte[]
        //export->local
        __response._Export("Export Path",bytes);

I have briefly listed some methods here, you can check out the 'API_Content' tutorial to learn about Colorful, or extend our framework, we have left a lot of extension interfaces, welcome to use!

-----



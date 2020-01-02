import React, { useState, useEffect } from "react";
import Recorder from 'recorder-js';
import ClipLoader from "react-spinners/ClipLoader";

export default function Step3(props) {
  const [recorder] = useState(
    new Recorder(new window.AudioContext(), {
      onAnalysed: (data) => {
        console.log("Recording: data:" + data);// An array of 255 Numbers, you can use this to visualize the audio stream (e.g. react-wave-stream)
      },
    })
  );

  const [countdownLeft, setCountdownLeft] = useState(3);
  const [isAnalyzing, setIsAnalyzing] = useState(false);

  const [word1, setWord1] = useState();
  const [word2, setWord2] = useState();
  const [word3, setWord3] = useState();
  const [word4, setWord4] = useState();
  const [word5, setWord5] = useState();
  const [word6, setWord6] = useState();


  const startKaraoke = () => {
    setTimeout(() => { setWord1('said') }, 0 );
    setTimeout(() => { setWord2('said') }, 500 );
    setTimeout(() => { setWord3('said') }, 1000 );
    setTimeout(() => { setWord4('said') }, 1400 );
    setTimeout(() => { setWord5('said') }, 1600 );
    setTimeout(() => { setWord6('said') }, 1800 );
    setTimeout(() => { setWord1('');
                       setWord2('');
                       setWord3('');
                       setWord4('');
                       setWord5('');
                       setWord6('') }, 3000 );
    setTimeout(() => { stopRecording() }, 3000 );
    setTimeout(() => { setIsAnalyzing(true) }, 3000 );
    setTimeout(() => { props.setStep(4) }, 5000 );
  }


  const initRecorder = () => {
    navigator.mediaDevices.getUserMedia({audio: true, video:false})
      .then(function(stream) {
        recorder.init(stream);
        console.log("Recording: initializing...");
      })
      .catch(err => console.log('Recording: failed. Unable to get stream...', err));
  }

  const startRecording = () => {
		recorder.start()
		  .then( console.log("Recording: started") );
  }

  const stopRecording = () => {
    recorder.stop()
      .then(({blob, buffer}) => {
        console.log("Recording: stopped");

        downloadRecording(blob);
      });
  }

  const downloadRecording = (blob) => {
    Recorder.download(blob, 'audiofile');
    /* alternatively: https://blog.addpipe.com/using-recorder-js-to-capture-wav-audio-in-your-html5-web-site/ */
  }


  //start countdown
  useEffect(() => {
    const interval = setInterval(() => {
      setCountdownLeft(countdownLeft => countdownLeft - 1);
    }, 1000);

    if (countdownLeft === 3 ) {
      initRecorder();//initialize recorder
    }

    if (countdownLeft === 1 ) {
      startRecording();//start recording
    }

    if (countdownLeft === 0 ) {
      clearInterval(interval);
      startKaraoke();//start karaoke
    }

    return () => clearInterval(interval);
  }, [countdownLeft]);

  return (
    <div>
      <h1 className="style-font">
        <span className={word1}>Bende </span>
        <span className={word2}>gij </span>
        <span className={word3}>een </span>
        <span className={word4}>Bra</span>
        <span className={word5}>ban</span>
        <span className={word6}>der?</span>
      </h1>
      <h2>
        {! isAnalyzing ? (
          (countdownLeft > 0 ? countdownLeft : 'GO!')
        ) : (
          <ClipLoader
            size={50} // or 150px
            color={"#000"}
            loading={isAnalyzing}
          />
        )}
      </h2>
    </div>
  );
}

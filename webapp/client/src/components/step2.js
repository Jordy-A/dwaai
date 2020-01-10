import React, { useState, useEffect } from "react";
import soundfile from '../assets/example.wav';

const intro = {
  en: 'Listen to an example first.',
  nl: 'Luister eerst naar een voorbeeld.',
  br: 'Eerst ekkes luisteren.',
}

const cta = {
  en: 'Now, try it yourself!',
  nl: 'Probeer het nu zelf.',
  br: 'En nou gij.',
}

export default function Step2(props) {
  const [word1, setWord1] = useState();
  const [word2, setWord2] = useState();
  const [word3, setWord3] = useState();
  const [word4, setWord4] = useState();
  const [word5, setWord5] = useState();
  const [word6, setWord6] = useState();
  const [button, setButton] = useState(false);

  const audio = new Audio(soundfile);

  const startKaraoke = () => {
    setTimeout(() => { audio.play() }, 0);
    setTimeout(() => { setWord1('said') }, 0 );
    setTimeout(() => { setWord2('said') }, 300 );
    setTimeout(() => { setWord3('said') }, 500 );
    setTimeout(() => { setWord4('said') }, 700 );
    setTimeout(() => { setWord5('said') }, 900 );
    setTimeout(() => { setWord6('said') }, 1100 );
    setTimeout(() => { setWord1('');
                       setWord2('');
                       setWord3('');
                       setWord4('');
                       setWord5('');
                       setWord6('') }, 2000 );
    setTimeout(() => { setButton(true) }, 2000 );
  }

  useEffect(() => {
    setTimeout(() => {startKaraoke() }, 1000 );
  }, []);

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
      {! button ? (
        <p>{intro[props.language]}</p>
      ) : (
        <button className="style-font" onClick={() => props.setStep(3)}>{cta[props.language]}</button>
      )}
    </div>
  );
}

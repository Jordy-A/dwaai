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
  const [karaokeIndex, setKaraokeIndex] = useState(0);
  const [button, setButton] = useState(false);

  const audio = new Audio(soundfile);

  const startKaraoke = () => {
    setTimeout(() => { audio.play() }, 0);
    setTimeout(() => { setKaraokeIndex(1) }, 0 );
    setTimeout(() => { setKaraokeIndex(2) }, 300 );
    setTimeout(() => { setKaraokeIndex(3) }, 500 );
    setTimeout(() => { setKaraokeIndex(4) }, 700 );
    setTimeout(() => { setKaraokeIndex(5) }, 900 );
    setTimeout(() => { setKaraokeIndex(6) }, 1100 );
    setTimeout(() => { setKaraokeIndex(0); }, 2000 );
    setTimeout(() => { setButton(true) }, 2000 );
  }

  useEffect(() => {
    setTimeout(() => {startKaraoke() }, 1000 );
  }, []);

  return (
    <div>
      <h1 className="style-font">
        <span className={karaokeIndex === 1 ? 'said' : null}>Bende </span>
        <span className={karaokeIndex === 2 ? 'said' : null}>gij </span>
        <span className={karaokeIndex === 3 ? 'said' : null}>een </span>
        <span className={karaokeIndex === 4 ? 'said' : null}>Bra</span>
        <span className={karaokeIndex === 5 ? 'said' : null}>ban</span>
        <span className={karaokeIndex === 6 ? 'said' : null}>der?</span>
      </h1>
      {! button ? (
        <p>{intro[props.language]}</p>
      ) : (
        <button className="style-font" onClick={() => props.setStep(3)}>{cta[props.language]}</button>
      )}
    </div>
  );
}

import React, { useState } from 'react';
import './App.css';
import Step1 from "./components/step1";
import Step2 from "./components/step2";
import Step3 from "./components/step3";
import Step4 from "./components/step4";

function App() {
  const [step, setStep] = useState(1);
  const [recordingResult, setRecordingResult] = useState();

  return (
    <div className="App">
      <div className="App-content">
        <img src="/eindhoven-vibes.png" className="App-logo" alt="logo" />

        { step === 1 && <Step1 setStep={setStep} /> }
        { step === 2 && <Step2 setStep={setStep} /> }
        { step === 3 && <Step3 setStep={setStep} setRecordingResult={setRecordingResult} /> }
        { step === 4 && <Step4 setStep={setStep} recordingResult={recordingResult} /> }

      </div>
    </div>
  );
}

export default App;

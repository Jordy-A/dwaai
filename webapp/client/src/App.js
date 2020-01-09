import React, { useState } from 'react';
import './App.css';
import Step0 from "./components/step0";
import Step1 from "./components/step1";
import Step2 from "./components/step2";
import Step3 from "./components/step3";
import Step4 from "./components/step4";

function App() {
  const [step, setStep] = useState(0);
  const [participantId, setParticipantId] = useState();
  const [recordingResult, setRecordingResult] = useState();
  const [visualisationResult, setVisualisationResult] = useState();

  return (
    <div className="App">
      <div className="App-content">
        <img src="/eindhoven-vibes.png" className="App-logo" alt="logo" />

        { step === 0 && <Step0 setStep={setStep} setParticipantId={setParticipantId} /> }
        { step === 1 && <Step1 setStep={setStep} /> }
        { step === 2 && <Step2 setStep={setStep} /> }
        { step === 3 && <Step3 setStep={setStep} setRecordingResult={setRecordingResult} setVisualisationResult={setVisualisationResult} /> }
        { step === 4 && <Step4 setStep={setStep} recordingResult={recordingResult} /> }

      </div>
    </div>
  );
}

export default App;

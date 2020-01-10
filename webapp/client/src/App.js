import React, { useState } from 'react';
import './App.css';
import Step0 from "./components/step0";
import Step1 from "./components/step1";
import Step2 from "./components/step2";
import Step3 from "./components/step3";
import Step4 from "./components/step4";
import LanguagePicker from './components/LanguagePicker';

function App() {
  const [step, setStep] = useState(0);
  const [participantId, setParticipantId] = useState();
  const [recordingResult, setRecordingResult] = useState();
  const [visualisationResult, setVisualisationResult] = useState();
  const [language, setLanguage] = useState('en');

  const state = {
    step,
    setStep,
    participantId,
    setParticipantId,
    recordingResult,
    setRecordingResult,
    visualisationResult,
    setVisualisationResult,
    language,
    setLanguage
  };

  return (
    <div className="App">
      <div className="App-content">
        <img src="/eindhoven-vibes.png" className="App-logo" alt="logo" />
        <LanguagePicker {...state} />

        { step === 0 && <Step0 {...state} /> }
        { step === 1 && <Step1 {...state} /> }
        { step === 2 && <Step2 {...state} /> }
        { step === 3 && <Step3 {...state} /> }
        { step === 4 && <Step4 {...state} /> }

      </div>
    </div>
  );
}

export default App;

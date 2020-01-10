import React, { Component } from "react";
import Recorder from 'recorder-js';
import ClipLoader from "react-spinners/ClipLoader";
import { motion } from 'framer-motion';

export default class Step3 extends Component {
  countdownInterval = null;
  recorder = null;
  analysisTick = 0;

  state = {
    countdownLeft: 3,
    isRecording: false,
    isAnalyzing: false,
    karaokeIndex: 0,
    visualisationValues: [],
  };

  constructor() {
    super();

    this.recorder = new Recorder(new window.AudioContext(), {
      onAnalysed: this.handleAnalysisTick
    });
  }

  componentDidMount() {
    // Initialize the recorder on mount
    this.initRecorder();

    // Start counting down when the component is mounted
    this.countdownInterval = setInterval(this.handleCountdownTick, 1000);
  }

  handleCountdownTick = () => {
    // Count down one more
    this.setState({ countdownLeft: this.state.countdownLeft - 1 });

    // Check if the countdown has reached zero
    if (this.state.countdownLeft === 0) {
      // If so, start recording and start karaoke
      this.startRecording();
      this.startKaraoke();
      clearInterval(this.countdownInterval);
    }
  }

  handleAnalysisTick = ({ data }) => {
    // Don't handle data unless we're recording
    if (!this.state.isRecording) {
      return;
    }

    // Increase analysis tick
    this.analysisTick += 1;

    // Exit function if we're not at a particular tick
    if (this.analysisTick % 3 !== 0) {
      return;
    }

    // Calculate mean value across frequencies
    const meanValue = data.reduce((acc, val) => acc + val, 0) / data.length;

    // Then apppend this value to the ones in state
    this.setState({
      visualisationValues: [
        ...this.state.visualisationValues,
        meanValue
      ]
    });
  }

  startKaraoke = () => {
    setTimeout(() => this.setState({ karaokeIndex: 1 }), 0 );
    setTimeout(() => this.setState({ karaokeIndex: 2 }), 300 );
    setTimeout(() => this.setState({ karaokeIndex: 3 }), 500 );
    setTimeout(() => this.setState({ karaokeIndex: 4 }), 700 );
    setTimeout(() => this.setState({ karaokeIndex: 5 }), 900 );
    setTimeout(() => this.setState({ karaokeIndex: 6 }), 1100 );
    setTimeout(() => this.setState({ karaokeIndex: 0 }), 2000 );
    setTimeout(() => this.stopRecording(), 2300 );
  }

  initRecorder = () => {
    navigator.mediaDevices.getUserMedia({ audio: true, video:false })
      .then((stream) => {
        this.recorder.init(stream);
        console.log("Recording: initializing...");
      })
      .catch(err => console.log('Recording: failed. Unable to get stream...', err));
  }

  startRecording = () => {
    // Set flag for recording
    this.setState({ isRecording: true });

    // Start the recorder and log to console
		this.recorder.start()
		  .then( console.log("Recording: started") );
  }

  stopRecording = () => {
    // Set flag for recording
    this.setState({ isRecording: false, isAnalyzing: true });

    // Stop the recorder
    this.recorder.stop()
      .then(({ blob, buffer}) => {
        // Log stopped recording and post blob to back-end
        console.log("Recording: stopped");
        return this.postRecording(blob);
      })
      .then((res) => {
        // Return result from back-end to container component
        this.props.setRecordingResult(res.result);
        this.props.setVisualisationResult(this.state.visualisationValues);
        this.props.setStep(4);
      })
      .catch(err => console.log(err));
  }

  postRecording = async (blob) => {
    // Prepare blob for sending using multipart forms
    var recordingData = new FormData();
    recordingData.append('audio', blob, Date.now() + '.wav');

    // Send request
    const response = await fetch('/recording', {
        method: 'POST',
        body: recordingData
      });
    const body = await response.json();

    if (response.status !== 200) {
      throw Error(body.message)
    }

    return body;
  };

  render() {
    const { countdownLeft, karaokeIndex, isAnalyzing, isRecording, visualisationValues } = this.state;

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
        {(isRecording || isAnalyzing) &&
          <div className="analysis">
            {visualisationValues.map((height, i) =>
              <motion.div
                key={i}
                animate={{ height }}
                positionTransition
              />
            )}
          </div>
        }
        <h2>
          {! isAnalyzing ? (
            (countdownLeft > 0 ? countdownLeft : '')
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
}

import React from "react";
import { motion } from 'framer-motion';
import eindhoven from '../assets/eindhoven.svg';
import eindhovenMuseum from '../assets/eindhoven-museum.svg';

export default class VisualizationCard extends React.Component {
  render() {

    const waveStyle = {
      backgroundColor: `hsl(${ Math.round(this.props.percentage/100 * 255) }, 100%, 50%)`,
    };

    return (
      <section className="postcard sheet padding-10mm">
        <div className="analysis">
          {this.props.visualisation.map((height, i) =>
            <motion.div
              key={i}
              animate={{ height }}
              positionTransition
              style={waveStyle}
            />
          )}
        </div>

        <h2>{ this.props.percentage }% Brabants</h2>

        <div className="footer">
          <img src={eindhoven} />
          <img src={eindhovenMuseum} />
        </div>
      </section>
    );
  }
}

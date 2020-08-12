import React, {Fragment} from 'react';
/** @jsx jsx */
import { jsx, css } from '@emotion/core';
import {BarLoader} from "react-spinners";
import axios from 'axios'

const options = [
  { value: 'random', label: 'Random' },
  { value: 'specific', label: 'Specific' },
]

const RequestLinkStyle = css`
  .redirect-form {
    font-size: 1.6rem;
  }

  .redirect-location-input {
    margin-top: 2rem;
    margin-bottom: 1rem;
    text-align: center;
    width: 50rem;
    display: inline-block;
    padding: 12px 20px;
  }
  
  .suffix-checkbox {
    margin-top: 1rem;
    margin-bottom: 1rem;
  }
  
  .redirect-location-label {
    display: block;
  }
  
  .suffix-checkbox-label {
    font-size: 1.2rem;
    bottom: .2rem;
    position: relative;
  }
  
  .redirect-location-div {
    margin-bottom: .5rem;
  }
  
  .suffix-checkbox-div {
    margin-top 2rem;
  }
  
  .suffix-div {
    margin-top: 4rem;
    margin-bottom: .5rem;
  }
  
  .generate-button-div {
    margin-top 2rem;
  }
  
  .suffix-input {
    width: 15rem;
  }
  
  .generate-button {
    color: #212121 !important;
    text-transform: lowercase;
    text-decoration: none;
    background: #f5f5f5;
    padding: 15px;
    display: inline-block;
    border: none;
    transition: all 0.4s ease 0s;
  }
`;

class RequestLink extends React.Component {
  state = { redirectLocation: '', uniqueSuffix: true, suffix: '', submitted: false, done: false };

  handleSubmit = async (event) => {
    event.preventDefault();
    this.setState({submitted: true})
    const data = { redirectLocation: this.state.redirectLocation }
    const resp = await axios.post(`https://api.lil.sh/v1/create`, data);
    this.props.onSubmit(resp.data);
    this.setState({ redirectLocation: '' });
  };

  handleCheck = async (event) => {
    this.setState({uniqueSuffix: !this.state.uniqueSuffix});
  }

  render() {
    return (
      <div css={[RequestLinkStyle]}>
        {!this.state.submitted ?
          <Fragment>
            <form className="redirect-form" onSubmit={this.handleSubmit}>
              <div className="redirect-location-div">
                <label className="redirect-location-label">your link
                  <br/>
                  <input
                    className="redirect-location-input"
                    type="url"
                    value={this.state.redirectLocation}
                    onChange={event => this.setState({ redirectLocation: event.target.value })}
                    placeholder="paste your url here"
                    required
                  />
                </label>
              </div>
              <div className="suffix-div">
                <label className="suffix-label">suffix
                  <br/>
                  <div className="suffix-checkbox-div">
                    <label className="suffix-checkbox-label">random </label>
                    <input className="suffix-checkbox" type="checkbox" onChange={this.handleCheck} defaultChecked={this.state.uniqueSuffix}/>
                  </div>
                  <div>
                    {this.state.uniqueSuffix ? null : <Fragment> <span style={{position: "relative"}}>lil.sh/</span><input
                      className="suffix-input"
                      type="text"
                      value={this.state.suffix}
                      onChange={event => this.setState({ suffix: event.target.value })}
                      required
                    /> </Fragment> }
                  </div>
                </label>
              </div>
              <br/>
              <div className="generate-button-div">
                <button className="generate-button">generate</button>
              </div>
            </form>
          </Fragment> :
          <div style={{ position: "fixed", top: "55%", left: "50%", transform: "translate(-50%, -50%)" }}>
            <BarLoader
              size={150}
              color={"#ffffff"}
              loading={true}
            />
          </div>
        }
      </div>
    );
  }
}

export default RequestLink;

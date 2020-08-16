import React, {Fragment} from 'react';
/** @jsx jsx */
import { jsx, css } from '@emotion/core';
import {BarLoader} from "react-spinners";
import axios from 'axios'
import { store } from 'react-notifications-component';
import {Link} from "react-router-dom";
import ReCaptcha, { loadReCaptcha } from 'react-recaptcha-v3'

const RequestLinkStyle = css`
  
`;

class RequestLink extends React.Component {
  state = { redirectLocation: '', randomSuffix: true, suffix: '', submitted: false, done: false, newUrl: '', errorMessage: '', typingTimeout: 0, typing: false, validSuffix: true };

  handleSubmit = async (event) => {
    event.preventDefault();
    this.setState({submitted: true})
    let data;
    if (this.state.randomSuffix === true) {
      data = {redirectLocation: this.state.redirectLocation}
    } else {
      data = { redirectLocation: this.state.redirectLocation, suffix: this.state.suffix }
    }
    try {
      const resp = await axios.post(`https://api.lil.sh/v1/create`, data);
      this.setState({ redirectLocation: '', randomSuffix: true, suffix: '', done: true, newUrl: resp.data.newUrl });
    } catch (apiError) {
      try {
        this.setState({errorMessage: "Error: " + apiError.response.data.errorMessage, submitted: false})
      }
      catch (notApiError) {
        this.setState({errorMessage: "Error: Internal Error", submitted: false})
      }
    }
  };

  handleCheck = async (event) => {
    this.setState({randomSuffix: !this.state.randomSuffix, validSuffix: true, suffix: "", errorMessage: ""});
  }

  checkSuffix = async () => {
    if (this.state.suffix.length < 3) {
      this.setState({validSuffix: false, errorMessage: "Suffix must be longer then 2 characters"})
      return
    }
    const resp = await axios.get('https://api.lil.sh/v1/check', {params: {suffix: this.state.suffix}});
    if (resp.data.exists === true) {
      this.setState({validSuffix: false, errorMessage: "Suffix taken"})
    } else {
      this.setState({validSuffix: true})
    }
  }

  changeSuffix = (event) => {
    if (this.state.typingTimeout) {
      this.setState({errorMessage: ""})
      clearTimeout(this.state.typingTimeout);
    }

    this.setState({
      suffix: event.target.value,
      typing: false,
      typingTimeout: setTimeout(this.checkSuffix, 500)
    });

  }

  componentDidMount() {
    loadReCaptcha("6LdnQr0ZAAAAAB-7wVzk2SVxb6JBcmZhj4jbOHG_");
  }

  render() {
    return (
      <div css={[RequestLinkStyle]}>
        {
          this.state.done ?
            <Fragment>
              <div className="yourlink-div"> your lil link <br/> <br/>
              <a className="link-text" onClick={() => {navigator.clipboard.writeText("https://" + this.state.newUrl); store.addNotification({
                message: "Copied to clipboard!",
                type: "default",
                insert: "top",
                container: "top-right",
                dismiss: {
                  duration: 2000
                }
              });} }>{this.state.newUrl}</a> <br/>
              <div className="make-another-div">
                <Link to ='/info' >
                  <button className="app-button" style={{marginRight: ".5rem"}}>info</button>
                </Link>
                <button className="app-button" style={{marginLeft: ".5rem"}} onClick={() => {this.setState({done: false, submitted: false })}}>make another</button>
              </div>
              </div>
            </Fragment>  : <Fragment>
        {!this.state.submitted ?
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
                    <input className="suffix-checkbox" type="checkbox" onChange={this.handleCheck} defaultChecked={this.state.randomSuffix}/>
                  </div>
                  <div>
                    {this.state.randomSuffix ? null : <Fragment> <span style={{position: "relative"}}>lil.sh/</span><input
                      className="suffix-input"
                      type="text"
                      value={this.state.suffix}
                      onChange={this.changeSuffix}
                      required
                    /> </Fragment> }
                  </div>
                </label>
              </div>
              <br/>
              <div className="generate-button-div">
                <button className="g-recaptcha app-button"
                        data-sitekey="6LdnQr0ZAAAAAB-7wVzk2SVxb6JBcmZhj4jbOHG_"
                        data-callback='onSubmit'
                        data-action='submit' disabled={!this.state.validSuffix} className="app-button">generate</button>
              </div>
              <br/>
              <div className="error-message-div">
                {this.state.errorMessage}
              </div>
            </form> :
          <div style={{ position: "fixed", top: "55%", left: "50%", transform: "translate(-50%, -50%)" }}>
            <BarLoader
              size={150}
              color={"#616161"}
              loading={true}
            />
          </div>
        }
      </Fragment>}
      </div>
    );
  }
}

export default RequestLink;

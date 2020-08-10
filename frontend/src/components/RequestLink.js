import React from 'react';
/** @jsx jsx */
import { jsx, css } from '@emotion/core';

const RequestLinkStyle = css`
  .redirect-location-input {
    margin-top: .5rem;
    margin-bottom: .5rem;
    text-align: left;
    width: 40rem;
  }
  
`;

class RequestLink extends React.Component {
  state = { redirectLocation: 'http://' };

  handleSubmit = async (event) => {
    event.preventDefault();
    const resp = await axios.get(`https://api.github.com/users/${this.state.redirectLocation}`);
    this.props.onSubmit(resp.data);
    this.setState({ redirectLocation: '' });
  };

  render() {
    return (
      <div css={[RequestLinkStyle]}>
        <form onSubmit={this.handleSubmit}>
          <input
            className="redirect-location-input"
            type="text"
            value={this.state.redirectLocation}
            onChange={event => this.setState({ redirectLocation: event.target.value })}
            placeholder="Redirect To?"
            required
          />
          <br/>
          <button>Create Short Link</button>
        </form>
      </div>
    );
  }
}

export default RequestLink;

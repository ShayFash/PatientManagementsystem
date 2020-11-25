import React from 'react';

class NewNote extends React.Component {
    constructor(props) {
        super();
        this.state={
            noteText: "",
            diagnosisText: ""
        };
        this.handleChange = this.handleChange.bind(this);
    }

    handleChange(event) {
        const {name, value} = event.target;
        this.setState({[name]: value})
    }

    render() {
        return (
            <form>
                <textarea className="largeTextBox"
                placeholder="Insert Text"
                name="noteText" 
                value={this.state.noteText}
                onChange={this.handleChange}
                >
                </textarea>

                <br />
                <input className="smallTextBox"
                type="text" 
                placeholder="Diagnosis"
                name="diagnosisText"
                value={this.state.diagnosisText}
                onChange={this.handleChange}
                >
                </input>
            </form>
        )
    }
}

export default NewNote;
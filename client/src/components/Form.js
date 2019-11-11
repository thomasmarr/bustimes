import React, { useState } from 'react'

import * as S from './Styles'

const Form = (props) => {
    const [input, setInput] = useState('')
    return (
        <>
            <p>Please enter an SMS stop code below.</p>
            <form onSubmit={e => {
                e.preventDefault()
                props.history.push(`/livearrivals/${input}`)
            }}>
                <S.inputField className="input-field">
                    <S.Input
                        id="smscode"
                        name="smscode"
                        type="number"
                        className="validate"
                        min="10000"
                        max="99999"
                        step="1"
                        value={input}
                        onChange={e => setInput(e.target.value)}
                    />
                    <label htmlFor="smscode">Stop SMS Code</label>
                </S.inputField>
                <S.Button type="submit" className="btn waves-effect waves-light">
                    Submit
                    <i className="material-icons right">send</i>
                </S.Button>
            </form>
        </>
    )
}

export default Form
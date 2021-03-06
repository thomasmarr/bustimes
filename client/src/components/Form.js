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
                <S.InputField className="input-field">
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
                </S.InputField>
                <S.Button type="submit" className="btn waves-effect waves-light">
                    Submit
                    <i className="material-icons right">send</i>
                </S.Button>
            </form>
            <S.SubtlePara>Alternatively, please <S.SubtleLink to="/livearrivals/naptan/490009333W">click here</S.SubtleLink> for a demo using a fixed naptan ID.</S.SubtlePara>
        </>
    )
}

export default Form
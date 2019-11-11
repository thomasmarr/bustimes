import styled from 'styled-components'

//Form Styles

export const inputField = styled.div`
    label {
        color: ${props => props.theme.primaryFontColor};
    }
    input[type=number]:focus + label {
        color: ${props => props.theme.primaryFontColor};
    }
    input[type=number]:focus {
        border-bottom: 1px solid ${props => props.theme.inputBorderColor};
        box-shadow: 0 1px 0 0 ${props => props.theme.inputShadowColor};
    }
    input[type=number].valid {
        border-bottom: 1px solid ${props => props.theme.inputBorderColor};
        box-shadow: 0 1px 0 0 ${props => props.theme.inputShadowColor};
    }
    input[type=number].invalid {
        border-bottom: 1px solid ${props => props.theme.inputBorderColor};
        box-shadow: 0 1px 0 0 ${props => props.theme.inputShadowColor};
    }
    .prefix.active {
        color: ${props => props.theme.primaryFontColor};
    }
    input[type=number]:not(.browser-default):focus:not([readonly])+label{
        color: ${props => props.theme.primaryFontColor};
    }
    input[type=number]:not(.broswer-default):focus:not([readonly]){
        border-bottom: 1px solid ${props => props.theme.inputBorderColor};
        box-shadow: 0 1px 0 0 ${props => props.theme.inputShadowColor};
    }
`

export const Input = styled.input`
    color:${props => props.theme.primaryFontColor};
`

export const Button = styled.button`
    background-color: ${props => props.theme.btnColor};
`
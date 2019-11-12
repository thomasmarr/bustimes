import styled from 'styled-components'
import { Link } from 'react-router-dom'

//Form Styles

export const InputField = styled.div`
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
    input[type=number]::-webkit-inner-spin-button, 
    input[type=number]::-webkit-outer-spin-button { 
    -webkit-appearance: none; 
    margin: 0; 
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
    &&& {
        background-color: ${props => props.theme.btnColor};
    }
`

//Arrivals styles

export const DataWrapper = styled.div`
    margin: auto;
    font-family: '${props => props.theme.dataFont}', Arial, sans-serif;
    font-size: 28px;
    color: ${props => props.theme.dataFontColor};
    background-color: ${props => props.theme.dataBgColor};
    max-width:650px;
    margin-bottom: 20px;
`

export const LineWrapper = styled.div`
    grid-template-columns: 0.5fr 4fr 1fr;
    display: grid;
`

export const DataLeft = styled.div`
    margin: 0 0 0 10px;
    min-width:45px;
`
export const DataMiddle = styled.div`
    margin: 0 15px 0 15px;
    white-space: nowrap;
    overflow-x: scroll;
    height: 45px;
    ::-webkit-scrollbar {
        display: none;
    }
`
export const DataRight = styled.div`
    margin: 0 10px 0 0;
    overflow-x: hidden;
    white-space: nowrap;
    overflow-x: scroll;
    min-width:50px;
    ::-webkit-scrollbar {
        display: none;
    }
`

//General Styles

export const Header = styled.h4`
    color:${props => props.theme.headerFontColor};
    ext-align:center;
`

export const SubtlePara = styled.p`
    color:${props => props.theme.subtleFontColor};
`

export const SubtleLink = styled(Link)`
    &&& {
        color:${props => props.theme.subtleLinkFontColor};
    }

`
export const PageHeader = styled.div`
    color:${props => props.theme.headerFontColor};
    text-align:center;
`

export const SubHeader = styled.div`
    font-size: 20px;
    color: ${props => props.theme.subheaderFontColor};
    margin: auto;
    max-width: 650px;
    padding: 5px;
`

export const Message = styled.div`
    text-align:center;
    margin-top:30px;
`

//Error styles
export const ErrorBox = styled.div`
    display: flex;
    align-items: center;
    justify-content: center;
    height: 80%;
    flex-direction: column
`

//Loading styles

export const LoadingWheel = styled.div`
    margin:30px auto;
    height: 150px;
    width: 150px;
    animation: rotate 0.8s infinite linear;
    border: 1px solid #aaa;
    border-right-color: transparent;
    border-radius: 50%;
    z-index: -10;
    @keyframes rotate {
        0% {
          transform: rotate(0deg);
        }
        100% {
          transform: rotate(360deg);
        }
      }
`

//Nav styles

export const NavWrap = styled.div`
    background-color: ${props => props.theme.navBgColor};
    color: ${props => props.theme.navFontColor};
`
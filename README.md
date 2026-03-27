<style>
  .leftLine {
    border-left : 2px dashed #4655652f;
    padding-left : 10px;
    margin-left : 4px;
  }
</style>

<h1>-onsole calculator</h1>


<br>


<h2>Навигация</h2>
<ul>
  <li>
    <a href="#aboutProject">
      <b>о проекте?</b>
    </a>
  </li>
  <li>
    <a href="#install">
      <b>install</b>
    </a>
  </li>
  <li>
    <a href="#mathSings">
      <b>добавление математическиз знаков?</b>
    </a>
  </li>
  <li>
    <a href="#future">
      <b>будущие нововведения</b>
    </a>
  </li>
</ul>


<br>
<br>
<br>


<h2 id="aboutProject">
  о чём этот проект
</h2><p>

  этот проект представляет собой консольный калькулятор написанный на пайтоне
  <br>соблюдая пять методов SOLID,
  <br>в этом калькуляторе у вас появляется возможность создавать свои
  <br>математические знаки, которые будут работать по вашим сценариям
  <br>а так же вы можете убирать существующие математические знаки,

  <br>так же в будущем мы хотим дать пользователю возможность писать полностью
  <br>свои математические конструкции, которые дадут возможность
  <br>тонко настраивать калькулятор под свои задачи

</p><br><br><br><br>

<h2 id="install">
  install
</h2><div>
  <details>
    <summary><h3>Linux</h3></summary>
    <div 
      class="leftLine" 
      style="padding-left : 20px;"
    >
      <details>
        <summary>arch подобные</summary>
        <div class="leftLine">
          <p style="margin: 0px;"><b>
            AUR
          </b></p>
            <p style="
              padding-left: 10px;
              border-left: 2px solid #4655652f;
            ">ещё нету</p>
        </div>
      </details>
      <details>
        <summary>debian подобные</summary>
        <div class="leftLine">
        <p>ещё не готово</p>
        </div>
      </details>
      <details>
        <summary>NixOS</summary>
        <div class="leftLine">
          <p>ещё не готово</p>
        </div>
      </details>
      <details>
        <summary>other</summary>
        <div class="leftLine">
          <p>инструкции ещё не готовы</p>
        </div>
      </details>
    </div>
  </details>
  <details>
    <summary><h3>Windows</h3></summary>
    <div class="leftLine">
      <p>ещё не готово</p>
    </div>
  </details>
  <details>
    <summary><h3>MacOS</h3></summary>
    <div class="leftLine">
      <p>ещё не готов</p>
    </div>
  </details>
</div>



<h2 id="mathSings">
  как и куда добавлять свои знаки?
</h2><p>

  что бы вы могли добавить свои знаки нужно открыть файл main.py
  <br>в каком-либо редакторе специлизируещемся на написании кода,
  <br>либо в блокноте или любом другом приложении,
  <br>в котором можно редактировать файлы;
  <br><br>

  после того как вы открыли файл, нужно найти строчки как на фото,
  <br>там есть разделитель в виде коментария, по нему можно определить
  <br>является ли эти строчки тем, что вам нужно;
  <br><br>

  если вы знаете язык программирования python, то читайте дальше,
  <br>а если вы его не знаете, то рекомендую прочесть
  <a href="./docs/python_manual.md"><br>
    <b>подробную инструкцию по добавлению своих математических знаков</b>
  </a>

  когда вы нашли нужный вам блок кода,
  вы можете добавить новый клас,
  <br>операясь на шаблон

</p>
<br><br>
  <img src="./images/mathSingClasses.png">
<br><br>

<h2 id="future">
  планы на будущее
</h2><ol>
  <li>добавление работы с выражениями содержащими скобки</li>
  <li>возможность построения графиков с помощью формул</li>
  <li>расширение математических конструкций колькулятора</li>
</ol>
# src/test_main.py
def test_main(capsys):
    from main import main
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello, Jenkins Pipeline!\n"

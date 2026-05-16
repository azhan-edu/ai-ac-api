from ai_ac_api.main import main


def test_main_output(capsys):
    main()
    captured = capsys.readouterr()
    assert "AI AC API initialized" in captured.out
